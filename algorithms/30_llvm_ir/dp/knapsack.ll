; ModuleID = 'algorithms/02_c/dp/knapsack.c'
source_filename = "algorithms/02_c/dp/knapsack.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local i32 @knapsack(i32 noundef %0, ptr noundef readonly captures(none) %1, ptr noundef readonly captures(none) %2, i32 noundef %3) local_unnamed_addr #0 {
  %5 = add i32 %3, 1
  %6 = zext i32 %5 to i64
  %7 = add i32 %0, 1
  %8 = zext i32 %7 to i64
  %9 = mul nuw i64 %6, %8
  %10 = alloca i32, i64 %9, align 16
  %11 = icmp slt i32 %3, 0
  br i1 %11, label %39, label %12

12:                                               ; preds = %4
  %13 = icmp slt i32 %0, 0
  %14 = icmp eq i32 %0, 0
  br label %15

15:                                               ; preds = %12, %46
  %16 = phi i64 [ 0, %12 ], [ %47, %46 ]
  br i1 %13, label %46, label %17

17:                                               ; preds = %15
  %18 = icmp eq i64 %16, 0
  %19 = add nsw i64 %16, -1
  %20 = mul nsw i64 %19, %8
  %21 = getelementptr inbounds i32, ptr %10, i64 %20
  %22 = mul nuw nsw i64 %16, %8
  %23 = getelementptr inbounds nuw i32, ptr %10, i64 %22
  %24 = getelementptr inbounds nuw i32, ptr %1, i64 %19
  %25 = getelementptr inbounds nuw i32, ptr %2, i64 %19
  store i32 0, ptr %23, align 4, !tbaa !5
  br i1 %18, label %38, label %26

26:                                               ; preds = %17
  %27 = load i32, ptr %24, align 4, !tbaa !5
  %28 = icmp sgt i32 %27, 0
  br i1 %28, label %38, label %29

29:                                               ; preds = %26
  %30 = sub nsw i32 0, %27
  %31 = zext nneg i32 %30 to i64
  %32 = getelementptr inbounds nuw i32, ptr %21, i64 %31
  %33 = load i32, ptr %32, align 4, !tbaa !5
  %34 = load i32, ptr %25, align 4, !tbaa !5
  %35 = add nsw i32 %34, %33
  %36 = icmp sgt i32 %35, 0
  br i1 %36, label %37, label %38

37:                                               ; preds = %29
  store i32 %35, ptr %23, align 4, !tbaa !5
  br label %38

38:                                               ; preds = %37, %29, %26, %17
  br i1 %14, label %46, label %49

39:                                               ; preds = %46, %4
  %40 = sext i32 %3 to i64
  %41 = mul nsw i64 %40, %8
  %42 = getelementptr inbounds i32, ptr %10, i64 %41
  %43 = sext i32 %0 to i64
  %44 = getelementptr inbounds i32, ptr %42, i64 %43
  %45 = load i32, ptr %44, align 4, !tbaa !5
  ret i32 %45

46:                                               ; preds = %70, %38, %15
  %47 = add nuw nsw i64 %16, 1
  %48 = icmp eq i64 %47, %6
  br i1 %48, label %39, label %15, !llvm.loop !9

49:                                               ; preds = %38, %70
  %50 = phi i64 [ %71, %70 ], [ 1, %38 ]
  br i1 %18, label %51, label %53

51:                                               ; preds = %49
  %52 = getelementptr inbounds nuw i32, ptr %23, i64 %50
  store i32 0, ptr %52, align 4, !tbaa !5
  br label %70

53:                                               ; preds = %49
  %54 = getelementptr inbounds nuw i32, ptr %21, i64 %50
  %55 = load i32, ptr %54, align 4, !tbaa !5
  %56 = getelementptr inbounds nuw i32, ptr %23, i64 %50
  store i32 %55, ptr %56, align 4, !tbaa !5
  %57 = load i32, ptr %24, align 4, !tbaa !5
  %58 = sext i32 %57 to i64
  %59 = icmp slt i64 %50, %58
  br i1 %59, label %70, label %60

60:                                               ; preds = %53
  %61 = trunc nuw nsw i64 %50 to i32
  %62 = sub nsw i32 %61, %57
  %63 = zext nneg i32 %62 to i64
  %64 = getelementptr inbounds nuw i32, ptr %21, i64 %63
  %65 = load i32, ptr %64, align 4, !tbaa !5
  %66 = load i32, ptr %25, align 4, !tbaa !5
  %67 = add nsw i32 %66, %65
  %68 = icmp sgt i32 %67, %55
  br i1 %68, label %69, label %70

69:                                               ; preds = %60
  store i32 %67, ptr %56, align 4, !tbaa !5
  br label %70

70:                                               ; preds = %51, %60, %69, %53
  %71 = add nuw nsw i64 %50, 1
  %72 = icmp eq i64 %71, %8
  br i1 %72, label %46, label %49, !llvm.loop !11
}

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

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
!11 = distinct !{!11, !10, !12}
!12 = !{!"llvm.loop.peeled.count", i32 1}
