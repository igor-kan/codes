; ModuleID = 'algorithms/02_c/strings/z_algorithm.c'
source_filename = "algorithms/02_c/strings/z_algorithm.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [8 x i8] c"abacaba\00", align 1
@.str.1 = private unnamed_addr constant [52 x i8] c"[C ZAlgorithm] FAILED at index %d: got %d, want %d\0A\00", align 1
@str = private unnamed_addr constant [45 x i8] c"[C ZAlgorithm] Z-array of \22abacaba\22 verified\00", align 1

; Function Attrs: nofree norecurse nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @z_function(ptr noundef readonly captures(none) %0, ptr noundef captures(none) initializes((0, 4)) %1) local_unnamed_addr #0 {
  %3 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %0) #7
  %4 = trunc i64 %3 to i32
  store i32 %4, ptr %1, align 4, !tbaa !5
  %5 = icmp sgt i32 %4, 1
  br i1 %5, label %6, label %9

6:                                                ; preds = %2
  %7 = and i64 %3, 2147483647
  %8 = and i64 %3, 2147483647
  br label %10

9:                                                ; preds = %50, %2
  ret void

10:                                               ; preds = %6, %50
  %11 = phi i64 [ 1, %6 ], [ %56, %50 ]
  %12 = phi i32 [ 0, %6 ], [ %55, %50 ]
  %13 = phi i32 [ 0, %6 ], [ %54, %50 ]
  %14 = zext nneg i32 %13 to i64
  %15 = icmp samesign ugt i64 %11, %14
  br i1 %15, label %25, label %16

16:                                               ; preds = %10
  %17 = sext i32 %12 to i64
  %18 = sub nsw i64 %11, %17
  %19 = getelementptr inbounds i32, ptr %1, i64 %18
  %20 = load i32, ptr %19, align 4, !tbaa !5
  %21 = trunc nuw nsw i64 %11 to i32
  %22 = sub nsw i32 %13, %21
  %23 = add nsw i32 %22, 1
  %24 = tail call i32 @llvm.smin.i32(i32 %20, i32 %23)
  br label %27

25:                                               ; preds = %10
  %26 = trunc nuw nsw i64 %11 to i32
  br label %27

27:                                               ; preds = %25, %16
  %28 = phi i32 [ %26, %25 ], [ %21, %16 ]
  %29 = phi i32 [ 0, %25 ], [ %24, %16 ]
  %30 = getelementptr inbounds nuw i32, ptr %1, i64 %11
  store i32 %29, ptr %30, align 4, !tbaa !5
  %31 = add nsw i32 %29, %28
  %32 = icmp slt i32 %31, %4
  br i1 %32, label %33, label %50

33:                                               ; preds = %27
  %34 = sext i32 %29 to i64
  br label %35

35:                                               ; preds = %33, %44
  %36 = phi i64 [ %34, %33 ], [ %45, %44 ]
  %37 = phi i32 [ %31, %33 ], [ %49, %44 ]
  %38 = getelementptr inbounds i8, ptr %0, i64 %36
  %39 = load i8, ptr %38, align 1, !tbaa !9
  %40 = sext i32 %37 to i64
  %41 = getelementptr inbounds i8, ptr %0, i64 %40
  %42 = load i8, ptr %41, align 1, !tbaa !9
  %43 = icmp eq i8 %39, %42
  br i1 %43, label %44, label %50

44:                                               ; preds = %35
  %45 = add nsw i64 %36, 1
  %46 = trunc nsw i64 %45 to i32
  store i32 %46, ptr %30, align 4, !tbaa !5
  %47 = add nsw i64 %45, %11
  %48 = icmp slt i64 %47, %7
  %49 = trunc nsw i64 %47 to i32
  br i1 %48, label %35, label %50, !llvm.loop !10

50:                                               ; preds = %35, %44, %27
  %51 = phi i32 [ %31, %27 ], [ %4, %44 ], [ %37, %35 ]
  %52 = add nsw i32 %51, -1
  %53 = icmp sgt i32 %52, %13
  %54 = tail call i32 @llvm.smax.i32(i32 %52, i32 %13)
  %55 = select i1 %53, i32 %28, i32 %12
  %56 = add nuw nsw i64 %11, 1
  %57 = icmp eq i64 %56, %8
  br i1 %57, label %9, label %10, !llvm.loop !12
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: read)
declare i64 @strlen(ptr noundef captures(none)) local_unnamed_addr #2

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #3 {
  %1 = alloca [100000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #8
  store i32 7, ptr %1, align 16, !tbaa !5
  br label %2

2:                                                ; preds = %42, %0
  %3 = phi i64 [ 1, %0 ], [ %48, %42 ]
  %4 = phi i32 [ 0, %0 ], [ %47, %42 ]
  %5 = phi i32 [ 0, %0 ], [ %46, %42 ]
  %6 = zext nneg i32 %5 to i64
  %7 = icmp samesign ugt i64 %3, %6
  br i1 %7, label %17, label %8

8:                                                ; preds = %2
  %9 = sext i32 %4 to i64
  %10 = sub nsw i64 %3, %9
  %11 = getelementptr inbounds i32, ptr %1, i64 %10
  %12 = load i32, ptr %11, align 4, !tbaa !5
  %13 = trunc nuw nsw i64 %3 to i32
  %14 = sub nsw i32 %5, %13
  %15 = add nsw i32 %14, 1
  %16 = tail call i32 @llvm.smin.i32(i32 %12, i32 %15)
  br label %19

17:                                               ; preds = %2
  %18 = trunc nuw nsw i64 %3 to i32
  br label %19

19:                                               ; preds = %17, %8
  %20 = phi i32 [ %18, %17 ], [ %13, %8 ]
  %21 = phi i32 [ 0, %17 ], [ %16, %8 ]
  %22 = getelementptr inbounds nuw i32, ptr %1, i64 %3
  store i32 %21, ptr %22, align 4, !tbaa !5
  %23 = add nsw i32 %21, %20
  %24 = icmp slt i32 %23, 7
  br i1 %24, label %25, label %42

25:                                               ; preds = %19
  %26 = sext i32 %21 to i64
  br label %27

27:                                               ; preds = %36, %25
  %28 = phi i64 [ %26, %25 ], [ %37, %36 ]
  %29 = phi i32 [ %23, %25 ], [ %41, %36 ]
  %30 = getelementptr inbounds i8, ptr @.str, i64 %28
  %31 = load i8, ptr %30, align 1, !tbaa !9
  %32 = sext i32 %29 to i64
  %33 = getelementptr inbounds i8, ptr @.str, i64 %32
  %34 = load i8, ptr %33, align 1, !tbaa !9
  %35 = icmp eq i8 %31, %34
  br i1 %35, label %36, label %42

36:                                               ; preds = %27
  %37 = add nsw i64 %28, 1
  %38 = trunc nsw i64 %37 to i32
  store i32 %38, ptr %22, align 4, !tbaa !5
  %39 = add nsw i64 %37, %3
  %40 = icmp slt i64 %39, 7
  %41 = trunc nsw i64 %39 to i32
  br i1 %40, label %27, label %42, !llvm.loop !10

42:                                               ; preds = %36, %27, %19
  %43 = phi i32 [ %23, %19 ], [ %29, %27 ], [ 7, %36 ]
  %44 = add nsw i32 %43, -1
  %45 = icmp sgt i32 %44, %5
  %46 = tail call i32 @llvm.smax.i32(i32 %44, i32 %5)
  %47 = select i1 %45, i32 %20, i32 %4
  %48 = add nuw nsw i64 %3, 1
  %49 = icmp eq i64 %48, 7
  br i1 %49, label %50, label %2, !llvm.loop !12

50:                                               ; preds = %42
  %51 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %52 = load i32, ptr %51, align 4, !tbaa !5
  %53 = icmp eq i32 %52, 0
  br i1 %53, label %54, label %76

54:                                               ; preds = %50
  %55 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %56 = load i32, ptr %55, align 8, !tbaa !5
  %57 = icmp eq i32 %56, 1
  br i1 %57, label %58, label %76

58:                                               ; preds = %54
  %59 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %60 = load i32, ptr %59, align 4, !tbaa !5
  %61 = icmp eq i32 %60, 0
  br i1 %61, label %62, label %76

62:                                               ; preds = %58
  %63 = getelementptr inbounds nuw i8, ptr %1, i64 16
  %64 = load i32, ptr %63, align 16, !tbaa !5
  %65 = icmp eq i32 %64, 3
  br i1 %65, label %66, label %76

66:                                               ; preds = %62
  %67 = getelementptr inbounds nuw i8, ptr %1, i64 20
  %68 = load i32, ptr %67, align 4, !tbaa !5
  %69 = icmp eq i32 %68, 0
  br i1 %69, label %70, label %76

70:                                               ; preds = %66
  %71 = getelementptr inbounds nuw i8, ptr %1, i64 24
  %72 = load i32, ptr %71, align 8, !tbaa !5
  %73 = icmp eq i32 %72, 1
  br i1 %73, label %74, label %76

74:                                               ; preds = %70
  %75 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %81

76:                                               ; preds = %70, %66, %62, %58, %54, %50
  %77 = phi i32 [ 6, %70 ], [ 1, %50 ], [ 2, %54 ], [ 3, %58 ], [ 4, %62 ], [ 5, %66 ]
  %78 = phi i32 [ %72, %70 ], [ %52, %50 ], [ %56, %54 ], [ %60, %58 ], [ %64, %62 ], [ %68, %66 ]
  %79 = phi i32 [ 1, %70 ], [ 0, %50 ], [ 1, %54 ], [ 0, %58 ], [ 3, %62 ], [ 0, %66 ]
  %80 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.1, i32 noundef %77, i32 noundef %78, i32 noundef %79)
  br label %81

81:                                               ; preds = %76, %74
  %82 = phi i32 [ 0, %74 ], [ 1, %76 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #8
  ret i32 %82
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #5

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #6

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #5

attributes #0 = { nofree norecurse nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: read) "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #6 = { nofree nounwind }
attributes #7 = { nounwind willreturn memory(read) }
attributes #8 = { nounwind }

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
!9 = !{!7, !7, i64 0}
!10 = distinct !{!10, !11}
!11 = !{!"llvm.loop.mustprogress"}
!12 = distinct !{!12, !11}
