; ModuleID = 'algorithms/02_c/math/ncr.c'
source_filename = "algorithms/02_c/math/ncr.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@fact = internal unnamed_addr global [1000001 x i64] zeroinitializer, align 16
@inv_fact = internal unnamed_addr global [1000001 x i64] zeroinitializer, align 16
@str = private unnamed_addr constant [42 x i8] c"[C NCR] nCr mod p via factorials verified\00", align 1
@str.2 = private unnamed_addr constant [46 x i8] c"[C NCR] FAILED: binomial coefficient mismatch\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local void @ncr_init(i32 noundef %0) local_unnamed_addr #0 {
  store i64 1, ptr @fact, align 16, !tbaa !9
  %2 = icmp slt i32 %0, 1
  br i1 %2, label %19, label %3

3:                                                ; preds = %1
  %4 = load i64, ptr @fact, align 16
  %5 = zext nneg i32 %0 to i64
  %6 = and i64 %5, 1
  %7 = icmp eq i32 %0, 1
  br i1 %7, label %12, label %8

8:                                                ; preds = %3
  %9 = and i64 %5, 2147483646
  br label %56

10:                                               ; preds = %56
  %11 = icmp eq i64 %6, 0
  br i1 %11, label %19, label %12

12:                                               ; preds = %10, %3
  %13 = phi i64 [ %4, %3 ], [ %66, %10 ]
  %14 = phi i64 [ 1, %3 ], [ %67, %10 ]
  %15 = icmp ne i64 %6, 0
  tail call void @llvm.assume(i1 %15)
  %16 = getelementptr i64, ptr @fact, i64 %14
  %17 = mul nsw i64 %13, %14
  %18 = srem i64 %17, 1000000007
  store i64 %18, ptr %16, align 8, !tbaa !9
  br label %19

19:                                               ; preds = %12, %10, %1
  %20 = sext i32 %0 to i64
  %21 = getelementptr inbounds i64, ptr @fact, i64 %20
  %22 = load i64, ptr %21, align 8, !tbaa !9
  br label %23

23:                                               ; preds = %33, %19
  %24 = phi i64 [ %22, %19 ], [ %35, %33 ]
  %25 = phi i64 [ 1, %19 ], [ %34, %33 ]
  %26 = phi i64 [ 1000000005, %19 ], [ %36, %33 ]
  %27 = srem i64 %24, 1000000007
  %28 = and i64 %26, 1
  %29 = icmp eq i64 %28, 0
  br i1 %29, label %33, label %30

30:                                               ; preds = %23
  %31 = mul nsw i64 %25, %27
  %32 = srem i64 %31, 1000000007
  br label %33

33:                                               ; preds = %30, %23
  %34 = phi i64 [ %32, %30 ], [ %25, %23 ]
  %35 = mul nsw i64 %27, %27
  %36 = lshr i64 %26, 1
  %37 = icmp eq i64 %36, 0
  br i1 %37, label %38, label %23, !llvm.loop !11

38:                                               ; preds = %33
  %39 = getelementptr inbounds i64, ptr @inv_fact, i64 %20
  store i64 %34, ptr %39, align 8, !tbaa !9
  %40 = icmp sgt i32 %0, 0
  br i1 %40, label %41, label %70

41:                                               ; preds = %38
  %42 = zext nneg i32 %0 to i64
  %43 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %42
  %44 = load i64, ptr %43, align 8, !tbaa !9
  %45 = and i64 %42, 1
  %46 = icmp eq i64 %45, 0
  br i1 %46, label %52, label %47

47:                                               ; preds = %41
  %48 = add nsw i64 %42, -1
  %49 = mul nsw i64 %44, %42
  %50 = srem i64 %49, 1000000007
  %51 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %48
  store i64 %50, ptr %51, align 8, !tbaa !9
  br label %52

52:                                               ; preds = %47, %41
  %53 = phi i64 [ %44, %41 ], [ %50, %47 ]
  %54 = phi i64 [ %42, %41 ], [ %48, %47 ]
  %55 = icmp eq i32 %0, 1
  br i1 %55, label %70, label %71

56:                                               ; preds = %56, %8
  %57 = phi i64 [ %4, %8 ], [ %66, %56 ]
  %58 = phi i64 [ 1, %8 ], [ %67, %56 ]
  %59 = phi i64 [ 0, %8 ], [ %68, %56 ]
  %60 = getelementptr i64, ptr @fact, i64 %58
  %61 = mul nsw i64 %57, %58
  %62 = srem i64 %61, 1000000007
  store i64 %62, ptr %60, align 8, !tbaa !9
  %63 = add nuw nsw i64 %58, 1
  %64 = getelementptr i64, ptr @fact, i64 %63
  %65 = mul nsw i64 %62, %63
  %66 = srem i64 %65, 1000000007
  store i64 %66, ptr %64, align 8, !tbaa !9
  %67 = add nuw nsw i64 %58, 2
  %68 = add i64 %59, 2
  %69 = icmp eq i64 %68, %9
  br i1 %69, label %10, label %56, !llvm.loop !13

70:                                               ; preds = %52, %71, %38
  ret void

71:                                               ; preds = %52, %71
  %72 = phi i64 [ %80, %71 ], [ %53, %52 ]
  %73 = phi i64 [ %78, %71 ], [ %54, %52 ]
  %74 = add nsw i64 %73, -1
  %75 = mul nsw i64 %72, %73
  %76 = srem i64 %75, 1000000007
  %77 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %74
  store i64 %76, ptr %77, align 8, !tbaa !9
  %78 = add nsw i64 %73, -2
  %79 = mul nsw i64 %76, %74
  %80 = srem i64 %79, 1000000007
  %81 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %78
  store i64 %80, ptr %81, align 8, !tbaa !9
  %82 = icmp sgt i64 %73, 2
  br i1 %82, label %71, label %70, !llvm.loop !14
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local range(i64 -1000000006, 1000000007) i64 @ncr(i32 noundef %0, i32 noundef %1) local_unnamed_addr #1 {
  %3 = icmp slt i32 %1, 0
  %4 = icmp sgt i32 %1, %0
  %5 = or i1 %3, %4
  br i1 %5, label %21, label %6

6:                                                ; preds = %2
  %7 = zext nneg i32 %0 to i64
  %8 = getelementptr inbounds nuw i64, ptr @fact, i64 %7
  %9 = load i64, ptr %8, align 8, !tbaa !9
  %10 = zext nneg i32 %1 to i64
  %11 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %10
  %12 = load i64, ptr %11, align 8, !tbaa !9
  %13 = mul nsw i64 %12, %9
  %14 = srem i64 %13, 1000000007
  %15 = sub nsw i32 %0, %1
  %16 = zext nneg i32 %15 to i64
  %17 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %16
  %18 = load i64, ptr %17, align 8, !tbaa !9
  %19 = mul nsw i64 %14, %18
  %20 = srem i64 %19, 1000000007
  br label %21

21:                                               ; preds = %2, %6
  %22 = phi i64 [ %20, %6 ], [ 0, %2 ]
  ret i64 %22
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  store i64 1, ptr @fact, align 16, !tbaa !9
  br label %19

1:                                                ; preds = %19
  %2 = load i64, ptr getelementptr inbounds nuw (i8, ptr @fact, i64 800), align 16, !tbaa !9
  br label %3

3:                                                ; preds = %13, %1
  %4 = phi i64 [ %2, %1 ], [ %15, %13 ]
  %5 = phi i64 [ 1, %1 ], [ %14, %13 ]
  %6 = phi i64 [ 1000000005, %1 ], [ %16, %13 ]
  %7 = srem i64 %4, 1000000007
  %8 = and i64 %6, 1
  %9 = icmp eq i64 %8, 0
  br i1 %9, label %13, label %10

10:                                               ; preds = %3
  %11 = mul nsw i64 %5, %7
  %12 = srem i64 %11, 1000000007
  br label %13

13:                                               ; preds = %10, %3
  %14 = phi i64 [ %12, %10 ], [ %5, %3 ]
  %15 = mul nsw i64 %7, %7
  %16 = lshr i64 %6, 1
  %17 = icmp eq i64 %16, 0
  br i1 %17, label %18, label %3, !llvm.loop !11

18:                                               ; preds = %13
  store i64 %14, ptr getelementptr inbounds nuw (i8, ptr @inv_fact, i64 800), align 16, !tbaa !9
  br label %31

19:                                               ; preds = %19, %0
  %20 = phi i64 [ 1, %0 ], [ %28, %19 ]
  %21 = phi i64 [ 1, %0 ], [ %29, %19 ]
  %22 = getelementptr i64, ptr @fact, i64 %21
  %23 = mul nsw i64 %20, %21
  %24 = srem i64 %23, 1000000007
  store i64 %24, ptr %22, align 8, !tbaa !9
  %25 = add nuw nsw i64 %21, 1
  %26 = getelementptr i64, ptr @fact, i64 %25
  %27 = mul nsw i64 %24, %25
  %28 = srem i64 %27, 1000000007
  store i64 %28, ptr %26, align 8, !tbaa !9
  %29 = add nuw nsw i64 %21, 2
  %30 = icmp eq i64 %29, 101
  br i1 %30, label %1, label %19, !llvm.loop !13

31:                                               ; preds = %31, %18
  %32 = phi i64 [ %14, %18 ], [ %40, %31 ]
  %33 = phi i64 [ 100, %18 ], [ %38, %31 ]
  %34 = add nsw i64 %33, -1
  %35 = mul nsw i64 %33, %32
  %36 = srem i64 %35, 1000000007
  %37 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %34
  store i64 %36, ptr %37, align 8, !tbaa !9
  %38 = add nsw i64 %33, -2
  %39 = mul nsw i64 %34, %36
  %40 = srem i64 %39, 1000000007
  %41 = getelementptr inbounds nuw i64, ptr @inv_fact, i64 %38
  store i64 %40, ptr %41, align 16, !tbaa !9
  %42 = icmp eq i64 %34, 1
  br i1 %42, label %43, label %31, !llvm.loop !14

43:                                               ; preds = %31
  %44 = load i64, ptr getelementptr inbounds nuw (i8, ptr @fact, i64 40), align 8, !tbaa !9
  %45 = load i64, ptr getelementptr inbounds nuw (i8, ptr @inv_fact, i64 16), align 16, !tbaa !9
  %46 = mul nsw i64 %45, %44
  %47 = srem i64 %46, 1000000007
  %48 = load i64, ptr getelementptr inbounds nuw (i8, ptr @inv_fact, i64 24), align 8, !tbaa !9
  %49 = mul nsw i64 %47, %48
  %50 = srem i64 %49, 1000000007
  %51 = icmp eq i64 %50, 10
  br i1 %51, label %52, label %70

52:                                               ; preds = %43
  %53 = load i64, ptr getelementptr inbounds nuw (i8, ptr @fact, i64 80), align 16, !tbaa !9
  %54 = mul nsw i64 %53, %48
  %55 = srem i64 %54, 1000000007
  %56 = load i64, ptr getelementptr inbounds nuw (i8, ptr @inv_fact, i64 56), align 8, !tbaa !9
  %57 = mul nsw i64 %55, %56
  %58 = srem i64 %57, 1000000007
  %59 = icmp eq i64 %58, 120
  br i1 %59, label %60, label %70

60:                                               ; preds = %52
  %61 = load i64, ptr @inv_fact, align 16, !tbaa !9
  %62 = mul nsw i64 %61, %53
  %63 = srem i64 %62, 1000000007
  %64 = load i64, ptr getelementptr inbounds nuw (i8, ptr @inv_fact, i64 80), align 16, !tbaa !9
  %65 = mul nsw i64 %63, %64
  %66 = srem i64 %65, 1000000007
  %67 = icmp ne i64 %66, 1
  %68 = select i1 %67, ptr @str.2, ptr @str
  %69 = zext i1 %67 to i32
  br label %70

70:                                               ; preds = %60, %43, %52
  %71 = phi ptr [ @str.2, %43 ], [ %68, %60 ], [ @str.2, %52 ]
  %72 = phi i32 [ 1, %43 ], [ %69, %60 ], [ 1, %52 ]
  %73 = tail call i32 @puts(ptr nonnull dereferenceable(1) %71)
  ret i32 %72
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind }
attributes #4 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !10, i64 0}
!10 = !{!"long long", !7, i64 0}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.mustprogress"}
!13 = distinct !{!13, !12}
!14 = distinct !{!14, !12}
