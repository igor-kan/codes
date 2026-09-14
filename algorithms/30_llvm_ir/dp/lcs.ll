; ModuleID = 'algorithms/02_c/dp/lcs.c'
source_filename = "algorithms/02_c/dp/lcs.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@lcs.dp = internal unnamed_addr global [1001 x [1001 x i32]] zeroinitializer, align 16

; Function Attrs: nofree norecurse nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local i32 @lcs(ptr noundef readonly captures(none) %0, ptr noundef readonly captures(none) %1) local_unnamed_addr #0 {
  %3 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %0) #3
  %4 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %1) #3
  %5 = and i64 %3, 2147483648
  %6 = icmp eq i64 %5, 0
  br i1 %6, label %7, label %24

7:                                                ; preds = %2
  %8 = and i64 %4, 2147483648
  %9 = icmp eq i64 %8, 0
  %10 = add i64 %4, 1
  %11 = add nuw nsw i64 %3, 1
  %12 = and i64 %11, 4294967295
  %13 = and i64 %10, 4294967295
  %14 = and i64 %4, 2147483647
  %15 = icmp eq i64 %14, 0
  br label %16

16:                                               ; preds = %7, %32
  %17 = phi i64 [ 0, %7 ], [ %33, %32 ]
  br i1 %9, label %18, label %32

18:                                               ; preds = %16
  %19 = icmp eq i64 %17, 0
  %20 = getelementptr inbounds nuw [1001 x i32], ptr @lcs.dp, i64 %17
  %21 = add nsw i64 %17, -1
  %22 = getelementptr inbounds i8, ptr %0, i64 %21
  %23 = getelementptr inbounds [1001 x i32], ptr @lcs.dp, i64 %21
  store i32 0, ptr %20, align 4, !tbaa !5
  br i1 %15, label %32, label %35

24:                                               ; preds = %32, %2
  %25 = shl i64 %3, 32
  %26 = ashr exact i64 %25, 32
  %27 = getelementptr inbounds [1001 x i32], ptr @lcs.dp, i64 %26
  %28 = shl i64 %4, 32
  %29 = ashr exact i64 %28, 30
  %30 = getelementptr inbounds i8, ptr %27, i64 %29
  %31 = load i32, ptr %30, align 4, !tbaa !5
  ret i32 %31

32:                                               ; preds = %53, %18, %16
  %33 = add nuw nsw i64 %17, 1
  %34 = icmp eq i64 %33, %12
  br i1 %34, label %24, label %16, !llvm.loop !9

35:                                               ; preds = %18, %53
  %36 = phi i64 [ %56, %53 ], [ 1, %18 ]
  br i1 %19, label %53, label %37

37:                                               ; preds = %35
  %38 = load i8, ptr %22, align 1, !tbaa !11
  %39 = add nsw i64 %36, -1
  %40 = getelementptr inbounds i8, ptr %1, i64 %39
  %41 = load i8, ptr %40, align 1, !tbaa !11
  %42 = icmp eq i8 %38, %41
  br i1 %42, label %43, label %47

43:                                               ; preds = %37
  %44 = getelementptr inbounds i32, ptr %23, i64 %39
  %45 = load i32, ptr %44, align 4, !tbaa !5
  %46 = add nsw i32 %45, 1
  br label %53

47:                                               ; preds = %37
  %48 = getelementptr inbounds nuw i32, ptr %23, i64 %36
  %49 = load i32, ptr %48, align 4, !tbaa !5
  %50 = getelementptr inbounds i32, ptr %20, i64 %39
  %51 = load i32, ptr %50, align 4, !tbaa !5
  %52 = tail call i32 @llvm.smax.i32(i32 %49, i32 %51)
  br label %53

53:                                               ; preds = %35, %47, %43
  %54 = phi i32 [ %46, %43 ], [ %52, %47 ], [ 0, %35 ]
  %55 = getelementptr inbounds nuw i32, ptr %20, i64 %36
  store i32 %54, ptr %55, align 4, !tbaa !5
  %56 = add nuw nsw i64 %36, 1
  %57 = icmp eq i64 %56, %13
  br i1 %57, label %32, label %35, !llvm.loop !12
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: read)
declare i64 @strlen(ptr noundef captures(none)) local_unnamed_addr #1

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #2

attributes #0 = { nofree norecurse nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: read) "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #3 = { nounwind willreturn memory(read) }

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
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = !{!7, !7, i64 0}
!12 = distinct !{!12, !10, !13}
!13 = !{!"llvm.loop.peeled.count", i32 1}
